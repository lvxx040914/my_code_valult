window.onload = initAll;
var usedNums = new Array(76);

function initAll() {
    if (document.getElementById) {
        document.getElementById("reload").onclick = anotherCard;
        newCard();
    } else {
        alert("Sorry, your browser doesn't support this script");
    }
}

function newCard() {
    for (var i = 0; i < 24; i++) {
        setSquare(i);
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

    do {
        newNum = colBasis + getNewNum() + 1;
    } while (usedNums[newNum]);

    usedNums[newNum] = true;
    document.getElementById(currSquare).innerHTML = newNum;
}

function getNewNum() {
    return Math.floor(Math.random() * 15);
}

function anotherCard() {
    // 重置已使用数字数组
    for (var i = 1; i < usedNums.length; i++) {
        usedNums[i] = false;
    }
    // 生成新卡片
    newCard();
    // 阻止链接默认跳转行为
    return false;
}