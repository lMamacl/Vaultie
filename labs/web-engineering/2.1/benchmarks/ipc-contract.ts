/**
 * Lab 2.1 — Wzorzec Bezpiecznego Kontraktu IPC dla Desktopu (Tauri & Electron)
 * 
 * Ten plik definiuje architektoniczny kontrakt typów pomiędzy
 * warstwą widoku (Renderer / Web View) a natywnym backendem (Rust / Node).
 */

// 1. Zdefiniowanie bezpiecznych operacji (Command Interface)
export interface DesktopApiContract {
  // Odczyt logów systemowych (asynchronicznie)
  getSystemLogs(): Promise<string[]>;

  // Zapis pliku z uprawnieniami piaskownicy
  saveConfiguration(config: Record<string, unknown>): Promise<{ success: boolean; path: string }>;

  // Transfer bufora binarnego bez narzutu serializacji JSON (np. obróbka obrazu/dźwięku)
  processBinaryBuffer(buffer: Uint8Array): Promise<Uint8Array>;
}

// 2. Implementacja dla Electrona (Preload Script z contextBridge)
// Używane w: src/preload.ts
export function setupElectronPreload(ipcRenderer: {
  invoke(channel: string, ...args: unknown[]): Promise<unknown>;
}) {
  const secureApi: DesktopApiContract = {
    async getSystemLogs() {
      return (await ipcRenderer.invoke('desktop:getLogs')) as string[];
    },
    async saveConfiguration(config) {
      return (await ipcRenderer.invoke('desktop:saveConfig', config)) as {
        success: boolean;
        path: string;
      };
    },
    async processBinaryBuffer(buffer) {
      // W Electronie przekazujemy Buffer bez konwersji na JSON
      return (await ipcRenderer.invoke('desktop:processBinary', buffer)) as Uint8Array;
    }
  };

  return secureApi;
}

// 3. Implementacja dla Tauri v2 (Rust Invoke Bridge)
// Używane w: src/services/tauri-bridge.ts
export function setupTauriBridge(invoke: <T>(cmd: string, args?: Record<string, unknown>) => Promise<T>) {
  const secureApi: DesktopApiContract = {
    async getSystemLogs() {
      // Tauri wywołuje komendę Rusta zdefiniowaną przez #[tauri::command]
      return await invoke<string[]>('get_system_logs');
    },
    async saveConfiguration(config) {
      return await invoke<{ success: boolean; path: string }>('save_configuration', { config });
    },
    async processBinaryBuffer(buffer) {
      // Tauri v2 obsługuje przekazywanie surowych bajtów przez zoptymalizowany kanał IPC
      return await invoke<Uint8Array>('process_binary_buffer', { buffer });
    }
  };

  return secureApi;
}
