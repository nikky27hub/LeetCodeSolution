/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        let timer;

        const timeoutPromise = new Promise((_, reject) => {
            timer = setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);
        });

        try {
            const result = await Promise.race([
                fn(...args),
                timeoutPromise
            ]);
            clearTimeout(timer);
            return result;
        } catch (err) {
            clearTimeout(timer);
            throw err;
        }
    };
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */