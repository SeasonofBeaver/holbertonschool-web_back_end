/* eslint-disable */
export default function updateUniqueItems(shoppingList) {
    if (!(shoppingList instanceof Map)) {
        throw new Error('Cannot process');
    }
    for (const [key, value] of shoppingList) {
        if (value === 1) {
            shoppingList.set(key, 100);
        }
    }
}