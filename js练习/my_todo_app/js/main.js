// 获取 DOM 元素
const input = document.getElementById('todo-input');
const addBtn = document.getElementById('add-btn');
const list = document.getElementById('todo-list');

// 初始加载
let todos = TodoStorage.fetch();
render();

// 添加任务
addBtn.onclick = () => {
    const text = input.value.trim();
    if (text) {
        todos.push({ id: Date.now(), text: text, done: false });
        input.value = '';
        update();
    }
};

// 渲染列表 (初学者必练：动态生成 DOM)
function render() {
    list.innerHTML = todos.map(todo => `
        <li class="${todo.done ? 'completed' : ''}">
            <span onclick="toggle(${todo.id})">${todo.text}</span>
            <button onclick="remove(${todo.id})">删除</button>
        </li>
    `).join('');
}

// 更新并保存
function update() {
    TodoStorage.save(todos);
    render();
}

// 简单的业务逻辑函数
window.toggle = (id) => {
    todos = todos.map(t => t.id === id ? {...t, done: !t.done} : t);
    update();
};

window.remove = (id) => {
    todos = todos.filter(t => t.id !== id);
    update();
};