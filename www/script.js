const tg = window.Telegram.WebApp;
const wv = window.Telegram.WebView;

console.dir(window.Telegram)

// основной цвет
tg.backgroundColor = "#000000"
tg.headerColor = "#000000"
tg.bottomBarColor = "#1d1d1d"

// нижний бар навигации
tg.MainButton.color = "#FF494C";
tg.MainButton.text = "В корзину";
tg.MainButton.textColor = "#FFFFFF"

tg.SecondaryButton.text = "Мои доставки";
tg.SecondaryButton.textColor = "#FF494C";

tg.SecondaryButton.show();
tg.MainButton.show();

let isOpened = false
let preventScroll = true

const sweetStreet = document.querySelector("header .sweet-street")
const sweetSeatch = document.querySelector("header .search")
const header = document.querySelector("header")
const input = document.querySelector(".search-bar div.input input")

const SerchBar = async (event) => {
    
    isOpened = !isOpened

    header.scrollTo({
        top: 0,
        left: isOpened ? header.clientWidth : 0,
        behavior: 'smooth'
    });
    if (isOpened) input.focus({ preventScroll: true })
    else input.blur()
}

document.querySelector("header .search").addEventListener("click", SerchBar)
document.querySelector("header .search-bar .close").addEventListener("click", SerchBar)