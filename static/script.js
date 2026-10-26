window.onload = loadBooks;

async function loadBooks() {
    const response = await fetch('/books');
    const data = await response.json();
    const list = document.getElementById('bookList');
    list.innerHTML = '';

    if (data.books.length === 0) {
        list.innerHTML = '<li>Пока нет добавленных книг.</li>';
        return;
    }

    data.books.forEach(book => {
        const li = document.createElement('li');
        li.textContent = `${book.title} — ${book.author} (${book.year})`;
        list.appendChild(li);
    });
}

async function addBook() {
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const year = parseInt(document.getElementById('year').value);

    if (!title || !author || !year) {
        alert('Заполните все поля!');
        return;
    }

    const response = await fetch('/books', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, author, year })
    });

    if (response.ok) {
        document.getElementById('title').value = '';
        document.getElementById('author').value = '';
        document.getElementById('year').value = '';
        loadBooks();
    } else {
        const error = await response.json();
        alert('Ошибка: ' + error.detail);
    }
}

async function searchByAuthor() {
    const author = document.getElementById('searchAuthor').value.trim();
    const list = document.getElementById('bookList');

    if (!author) {
        alert('Введите имя автора для поиска');
        return;
    }

    const response = await fetch(`/books/author/${encodeURIComponent(author)}`);
    const data = await response.json();
    
    list.innerHTML = '';
    if (data.count === 0) {
        list.innerHTML = `<li>Книг автора "${author}" не найдено.</li>`;
        return;
    }

    data.books.forEach(book => {
        const li = document.createElement('li');
        li.textContent = `${book.title} — ${book.author} (${book.year})`;
        list.appendChild(li);
    });
}