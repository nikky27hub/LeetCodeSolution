/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 */
var TimeLimitedCache = function () {
    this.cache = new Map();
};

TimeLimitedCache.prototype.set = function (key, value, duration) {
    const now = Date.now();
    const exists =
        this.cache.has(key) && this.cache.get(key).expire > now;

    this.cache.set(key, {
        value: value,
        expire: now + duration
    });

    return exists;
};

/**
 * @param {number} key
 * @return {number}
 */
TimeLimitedCache.prototype.get = function (key) {
    const now = Date.now();

    if (
        this.cache.has(key) &&
        this.cache.get(key).expire > now
    ) {
        return this.cache.get(key).value;
    }

    return -1;
};

/**
 * @return {number}
 */
TimeLimitedCache.prototype.count = function () {
    const now = Date.now();
    let cnt = 0;

    for (const { expire } of this.cache.values()) {
        if (expire > now) cnt++;
    }

    return cnt;
};

/**
 * const obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000)
 * obj.get(1)
 * obj.count()
 */