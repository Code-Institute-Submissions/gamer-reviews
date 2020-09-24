let xhr = new XMLHttpRequest();

xhr.open("GET", "http://www.gamespot.com/api/articles/?api_key=000baa7b080b00acf213f8f9b66c4b63ee0acbff&format=json");
xhr.send();
xhr.onload = () => {
    console.log(xhr);
    if (xhr.status == 200) {
        console.log(JSON.parse(xhr.response));
    } else {
        console.log(`error ${xhr.status} ${xhr.statusText}`);
    }
};