/* eslint-disable */
export default function updateUniqueItems(shoppingList) {
    if (!(shoppingList instanceof Map)) {
        throw new Error('Cannot process');
    }
    for (const [key, value] of map) {
        if (value === 1) {
            map.set(key, 100);
        }
    }
}