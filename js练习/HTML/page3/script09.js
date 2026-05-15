window.onload = initAll;
var usedNums = new Array(76);

function initAll() {
    if (document.getElementById) {
        for (var i = 0; i < 24; i++) {
            setSquare(i);
        }
    } else {
        alert("Sorry, your browser doesn't support this script");
    }
}

function setSquare(thisSquare) {
    var currSquare = "square" + thisSquare;
    var colPlace = new Array(
        0,0,0,0,0,
        1,1,1,1,1,
        2,2,2,2,
        3,3,3,3,3,
        4,4,4,4,4
    );
    var colBasis = colPlace[thisSquare] * 15;
    var newNum;

    // 核心修改：循环重试，直到找到未使用的数字
    do {
        newNum = colBasis + getNewNum() + 1;
    } while (usedNums[newNum]);

    usedNums[newNum] = true;
    document.getElementById(currSquare).innerHTML = newNum;
}

function getNewNum() {
    return Math.floor(Math.random() * 15);
}