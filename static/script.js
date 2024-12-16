fetch('/get_posts')
    .then(response => response.json())
    .then(posts => {
        const tableBody = document.getElementById('table-body');
        posts.forEach(post => {
            const row = `<tr><td>${post.time}</td><td>${post.message}</td></tr>`;
            tableBody.innerHTML += row;
        });
    });
