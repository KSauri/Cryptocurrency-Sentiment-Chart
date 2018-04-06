/**
 * Graphs will use data that only goes back so far.
 * The FixedQueue class provides a queue with a max length.
 * The queue is LIFO, and will update automatically once the max length is reached. 
 */
export class FixedQueue {
    constructor(maxLen) {
        this.maxLen = maxLen;
        this.values = [];
    }
    enqueue (value) {
        if (this.values.length < this.maxLen) {
            this.values.push(value);
        } else {
            this.values.shift();
            this.values.push(value);
        }
    }
    getValues () {
        return this.values;
    }
}