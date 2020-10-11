let xhr;
let data;
let myArticles;
let myArticlesPages = [];
let selectedPage;
let selectedIndex;
let startIndex;
let endIndex;
let pageIndex;
let pagingList;

xhr = new XMLHttpRequest();

xhr.open("GET", "http://www.gamespot.com/api/articles/?api_key=000baa7b080b00acf213f8f9b66c4b63ee0acbff&format=json&filter=publish_date:2020-09-01%7c2020-09-31&limit=15");
xhr.send();
xhr.onload = () => {
    if (xhr.status == 200) {
        data = JSON.parse(xhr.response);
    }
    else {
        console.log(`error ${xhr.status} ${xhr.statusText}`);
    }
    myArticles = data.results;
    console.log(myArticles);
    let pagesNumber = myArticles.length / 5;
    const pagesNumberRemainder = pagesNumber % 1;
    const pagesNumberWithoutRemainder = Math.floor(pagesNumber);
    if (pagesNumberRemainder > 0)
        pagesNumber = Number(pagesNumberWithoutRemainder) + 1;
    myArticlesPages = Array(pagesNumber)
        .fill(1)
        .map((x, i) => i + 1);
    startIndex = 0;
    endIndex = 5;
    selectedPage = 1;
    injectPagination();
    injectPage();
};

function injectPagination() {
    pagingList = `
            <li class="page-item pagination-btn"><a class="page-link" href="#" onclick="goPrevious()">Previous</a></li>
            <li class="page-item pagination-btn"><span class="page-link" id="spanSelectedPage">${selectedPage} | ${myArticlesPages.length}</span></li>
            <li class="page-item pagination-btn"><a class="page-link" href="#" onclick="goNext()">Next</a></li>`;

    document.getElementById("paging").innerHTML = pagingList;
}

function injectPage() {
    const list = myArticles.slice(startIndex, endIndex);
    console.log(list);
    document.getElementById("articles").innerHTML = list.map((i) => {
        return `
        <div class="col-4">
            <img src="${i.image.original}" class="article-img">
        </div>
        <div class="col-8">
            <a href="{{url_for('single_article')}}">
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
}

function goPrevious() {
    if (selectedPage != 1) {
        startIndex -= 5;
        endIndex -= 5;
        selectedPage--;
        injectPage();
        injectPagination();
    }
}

function goNext() {
    if (selectedPage < myArticlesPages.length) {
        startIndex += 5;
        endIndex += 5;
        selectedPage++;
        injectPage();
        injectPagination();
    }
}
