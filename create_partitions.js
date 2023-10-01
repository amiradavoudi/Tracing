// The algorithm for partitioning is based on the link below.
// https://stackoverflow.com/questions/54596127/how-to-find-all-partitions-of-a-multiset-where-each-part-has-distinct-elements


//File 'create_partitions.js' gets the file 'plausible_traces.txt' as its input and creates all the corresponding
// partitions, written to the file 'partitions.txt'. Note: A partition is defined in Section 6 of the paper.

function distribute(e, i, _comb){
    // No more e's
    if (e[1] == 0)
        return [_comb];
    // We're beyond the combination
    if (i == -1)
        return [_comb.concat([e])];
    let result = [];
    for (let c=1; c<=Math.min(_comb[i][1], e[1]); c++){
        let comb = _comb.map(x => x.slice());

        if (c == comb[i][1]){
            comb[i][0] += e[0];

        } else {
            comb[i][1] -= c;
            comb.push([comb[i][0] + e[0], c]);
        }
        result = result.concat(distribute([e[0], e[1] - c], i - 1, comb));
    }
    let comb = _comb.map(x => x.slice());
    return result.concat(distribute(e, i - 1, comb));
}

function f(arr){
    function g(i){
        if (i == 0)
            return [[arr[0]]];
        const combs = g(i - 1);
        let result = [];
        for (let comb of combs)
            result = result.concat(
                distribute(arr[i], comb.length - 1, comb));
        return result;
    }
    return g(arr.length - 1);
}

function create_partitions(arr){
    const rs = f(arr);
    const set = new Set();

    for (let r of rs){
        const _r = JSON.stringify(r);
        if (set.has(_r))
            console.log('Duplicate: ' + _r);
        set.add(_r);
    }

    let str = '';
    for (let r of set)
        str += '\n' + r
    str += '\n\n';

    // console.log(JSON.stringify(arr));
    // console.log(set.size + ' combinations:');
    // console.log(str);
    return set.size
}

// partition([['A', 2], ['B', 2], ['C', 2], ['D', 1], ['E', 1]]);

const fs = require('fs')
fs.readFile('plausible_traces.txt', (err, inputD) => {
    if (err) throw err;
    const all_wallets_plaus_traces = inputD.toString().split(';');
    const all_number_of_plausible_cycles = [];
    for (let i = 0; i < all_wallets_plaus_traces.length - 1; i++) {
        plau_traces = eval(all_wallets_plaus_traces[i])
        const number_of_plausible_cycles = [];
        for (let j = 0; j < (plau_traces.length); j++) {
            plaus_trace = plau_traces[j]
            console.log(plaus_trace);
            num_plaus_cycles = create_partitions(plaus_trace);
            number_of_plausible_cycles[j] = num_plaus_cycles
        }

        console.log(number_of_plausible_cycles)
        console.log("-----------------------------------")
        all_number_of_plausible_cycles[i] = number_of_plausible_cycles
    }
    console.log(all_number_of_plausible_cycles)
    var file = fs.createWriteStream('partitions.txt');
    file.on('error', function(err) { /* error handling */ });
    all_number_of_plausible_cycles.forEach(function(v) { file.write(v.join(', ') + '\n'); });
    file.end();
})



