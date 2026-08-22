/** Shared DTO — lab 1.3: zmiana tutaj widoczna w apps/web przez workspace:* */

export const USER_DTO_SCHEMA_VERSION = 1;

/**
 * @param {string} id
 * @param {string} email
 */
export function createUserDto(id, email) {
  if (!id || !email) {
    throw new Error("UserDto requires id and email");
  }
  return { id, email, schemaVersion: USER_DTO_SCHEMA_VERSION };
}
