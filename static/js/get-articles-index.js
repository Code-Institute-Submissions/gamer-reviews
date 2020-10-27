let xhr;
var myArticles;
var data;

xhr = new XMLHttpRequest();
// https://cors-anywhere.herokuapp.com is a proxy server that adds CORS header to a request
//api request for articles on home page using gamespot api
xhr.open("GET", "https://cors-anywhere.herokuapp.com/http://www.gamespot.com/api/articles/?api_key=000baa7b080b00acf213f8f9b66c4b63ee0acbff&format=json&filter=publish_date:2020-09-01%7c2020-09-31&limit=3");
xhr.send();
xhr.onload = () => {
    console.log(xhr);
    if (xhr.status == 200) {
        data = JSON.parse(xhr.response);
    }
    else {
        console.log(`error ${xhr.status} ${xhr.statusText}`);
    }
    //stores data in myArticles variable 
    myArticles = data.results;
    // a loop displays articles on articles.html using template literals and a modal to display articles
    document.getElementById("articles").innerHTML = myArticles.map((i) => {
        return `
        <div class="col-sm-4">
            <img src="${i.image.original}" class="article-img">
        </div>
        <div class="col-sm-8">
                <h4 class="articles-heading">${i.title}</h4>
            <h6 class="articles-heading">${i.publish_date}</h6>
            <div>
                <p class="article-content">${i.deck}</p>
            </div>
            <div>
                <button class="btn btn-success read-article-btn" data-toggle="modal" data-target="#modal${i.id}">Read Article</button>
            </div>
        </div>
        <div class="modal fade" id="modal${i.id}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h4>${i.title}</h4>
                </div>
                <div class="modal-body row">
                    <div class="col-12">
                        <img src="${i.image.original}" class="article-img-modal">
                    </div>
                </div>
                <div class="row">
                    <div class="col-12 modal-article-area">
                        <p><strong>Publish Date: </strong>${i.publish_date}</p>
                        <article>${i.deck}</article>
                    </div>
                </div>
                <div class="row">
                    <div class="col-12 full-article-url">
                        <p><strong>View Full Article:</strong></p>
                        <a href="${i.site_detail_url}" target="_blank"><p>${i.site_detail_url}</p></a>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-success close-modal-btn" data-dismiss="modal">Close</button>
                </div>
            </div>
          </div>
        </div>`;
    }).join('');
};
