/* eslint-disable */
import Currency from "./3-currency.js"

export default class Pricing {
    constructor(amount, currency) {
        if (typeof amount !== 'number') {
            throw new TypeError('Amount must be a number');
        }
        this._amount = amount;
        if (!(currency instanceof Currency)) {
            throw new TypeError('Currency must be a currency');
        }
        this._currency = currency;
    }
    get amount() {
        return this._amount
    }

    set amount(value) {
        if (typeof value !== 'number') {
            throw new TypeError('Amount must be a number');
        }
            this._amount = value;
    }

    get currency() {
        return this._currency
    }

    set currency(value) {
        if (!(value instanceof Currency)) {
            throw new TypeError('Currency must be a currency');
        }
        this._currency = value;
    }

    displayFullPrice() {
        return `${this._amount} ${this._currency.name} (${this._currency.code})`
    }

    static convertPrice(amount, conversionRate) {
        if (typeof amount !== 'number' || typeof conversionRate !== 'number')
            throw new TypeError('Amount and ConversionRate must be a Number');
        return amount * conversionRate
    }
}