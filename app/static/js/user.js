const sidebar = $('#sidebar-bg').get(0);
const main = $('#main').get(0);

function toggleSidebar() {
    if (sidebar.style.display === "none") {
        main.style.marginLeft="12%";
        sidebar.style.width="12%";
        sidebar.style.display = "block";
    } else {
        main.style.marginLeft="0%";
        sidebar.style.display = "none";
    }
}


function bookSearch() {
    var search = document.getElementById('search').value
    document.getElementById('results').innerHTML = ""
    console.log(search)
    $.ajax({
        url: "https://www.googleapis.com/books/v1/volumes?q=" + search +"&key=AIzaSyB9Q2aWWmNUHPG60ZK3RQczqe0mt_TAyHc",
        dataType: "json",
        success: function(books) {
            for (i = 0; i < books.items.length; i++) {
              results.innerHTML += "<h2>" + books.items[i].volumeInfo.title + "</h2>"
            }
            console.log(books)
        },
        type: 'GET'
    });
}
