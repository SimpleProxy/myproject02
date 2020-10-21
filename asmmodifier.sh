#!/bin/sh
# sed script to modify the asm code used to test the performance of the Hack VM
# ???: use (g)awk instead of sed

NUM=${1:-1}
#sed -i '/finthis/s/replacethis/withthis/g'
#sed -i -E '/set\ RAM\[0\]/s/\ [0-9]{2}/\ $NUM/' ./vm_code/test/Factorial.tst
#touch ./vm_code/test/test.txt
#awk ''
sed -i -E "/^set\ RAM\[1\]\ [0-9]+/s/[0-9]+/$NUM/2" \
    ./vm_code/test/Factorial.tst
#./vm_code/test/test.txt
