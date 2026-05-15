// 负责本地存储的存取
const TodoStorage = {
    save(todos) {
        localStorage.setItem('my-todos', JSON.stringify(todos));
    },
    fetch() {
        return JSON.parse(localStorage.getItem('my-todos') || '[]');
    }
};