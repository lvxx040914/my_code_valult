// 第一步：当窗口加载完毕时，执行 initAll 函数
window.onload = initAll;

function initAll() {
    // 第二步：通过 ID 找到 HTML 里的那个链接 (<a> 标签)
    var redirectLink = document.getElementById("redirect");
    
    // 检查一下是否真的找到了这个元素，防止报错
    if (redirectLink) {
        // 第三步：当用户点击这个链接时，执行 initRedirect 函数
        redirectLink.onclick = initRedirect;
    }
}

function initRedirect() {
    // 第四步：改变当前窗口的地址，跳转到新页面
    // 请确保你本地也有一个叫 jswelcome.html 的文件，否则会报 404 错误
    window.location = "jswelcome.html";
    
    // 第五步：【关键】返回 false 告诉浏览器：“不要执行 HTML 里的 href 跳转”
    return false;
}