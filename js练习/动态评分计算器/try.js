// 1. 获取 DOM 元素 (使用 const)
const btn = document.querySelector('#calcBtn');
const input = document.querySelector('#scoresInput');
const avgText = document.querySelector('#avgText');
const failList = document.querySelector('#failList');

// 2. 绑定点击事件 (使用箭头函数)
btn.addEventListener('click', () => {
    // 获取输入值并转成数组 (使用 split 和 map)
    const rawValue = input.value; 
    const scores = rawValue.split(',').map(num => Number(num.trim()));

    // 3. 计算平均分 (使用 reduce)
    const total = scores.reduce((sum, s) => sum + s, 0);
    const avg = total / scores.length;
    
    // 更新 DOM (使用模板字符串)
    avgText.innerText = `${avg.toFixed(2)} 分`;

    // 4. 找出不及格的分数 (使用 filter)
    const fails = scores.filter(s => s < 60);
    
    // 渲染不及格列表
    failList.innerHTML = `<p style="color:red">不及格的有：${fails.join(', ')}</p>`;
});