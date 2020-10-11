let xhr;
var myArticles;
var data;

xhr = new XMLHttpRequest();

xhr.open("GET", "http://www.gamespot.com/api/articles/?api_key=000baa7b080b00acf213f8f9b66c4b63ee0acbff&format=json&filter=publish_date:2020-09-01%7c2020-09-31&limit=3");
xhr.send();
xhr.onload = () => {
    console.log(xhr);
    if (xhr.status == 200) {
        data = JSON.parse(xhr.response);
    } else {
        console.log(`error ${xhr.status} ${xhr.statusText}`);
    }
    myArticles = data.results;
    console.log(myArticles);
    document.getElementById("articles").innerHTML = myArticles.map((i) => {
        return `
        <div class="col-4">
            <img src="${i.image.original}" class="article-img">
        </div>
        <div class="col-8">
            <a href="#">
                <h4 class="articles-heading">${i.title}</h4>
            </a>
            <h6 class="articles-heading">${i.publish_date}</h6>
            <div>
                <p class="article-content">${i.deck}</p>
            </div>
            <div>
                <button class="btn btn-success read-article-btn">Read Article</button>
            </div>
        </div>`;
    }).join('');
};

