use std::io::{self, Read};
use std::collections::HashSet;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut iter = input.split_whitespace();

    let t: usize = iter.next().unwrap().parse().unwrap();

    let mut outputs = Vec::with_capacity(t);

    for _ in 0..t {
        let n: usize = iter.next().unwrap().parse().unwrap();

        let mut arr = Vec::with_capacity(n);
        for _ in 0..n {
            let x: i64 = iter.next().unwrap().parse().unwrap();
            arr.push(x);
        }

        let mut seen = HashSet::new();
        let mut curr: i64 = 0;
        let mut flag = true;
        let mut found = false;

        for &val in arr.iter() {
            if flag {
                curr += val;
            } else {
                curr -= val;
            }
            flag = !flag; 

            if curr == 0 || seen.contains(&curr) {
                found = true;
                break;
            }
            seen.insert(curr);
        }

        if found {
            outputs.push("YES");
        } else {
            outputs.push("NO");
        }
    }

    println!("{}", outputs.join("\n"));
}
