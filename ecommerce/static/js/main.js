// side menu
var btnMenu = document.querySelector(".menu-btn");
var menu = document.querySelector(".menu");

btnMenu.addEventListener("click", function () {
    if (menu.style.marginTop == "0px") {
        menu.style.opacity = "0";
        menu.style.visibility = "hidden";

        menu.style.marginTop = "-22em";
    } else {
        menu.style.opacity = "1";
        menu.style.visibility = "visible";
        menu.style.marginTop = "0px";
    }
});

// scroll top
var scrollTop = document.querySelector(".scroll");

window.onscroll = function () {
    if (scrollY > "750") {
        scrollTop.style.right = "35px";
    } else {
        scrollTop.style.right = "-35px";
    }
};

scrollTop.onclick = function () {
    window.scrollTo({
        top: 0,
        behavior: "smooth",
    });
};

// checkout

// var checkBody = document.querySelectorAll(".check-body");
// var remove = document.querySelectorAll(".remove");
//
// for (let i = 0; i < remove.length; i++) {
//     remove[i].onclick = function () {
//         checkBody[i].remove();
//     };
// }

// accounts-menu

var btnAccounts = document.querySelector(".accounts");
var btnAccountsSide = document.querySelector("#btn-accounts-side");
var accountsMenu = document.querySelector(".accounts-menu");
var accountsSideMenu = document.querySelector(".accounts-side-menu");

console.log(btnAccounts);

btnAccounts.onclick = function () {
    if (accountsMenu.style.display == "block") {
        accountsMenu.style.display = "none";
    } else {
        accountsMenu.style.display = "block";
    }
};

btnAccountsSide.onclick = function () {
    if (accountsSideMenu.style.display == "block") {
        accountsSideMenu.style.display = "none";
    } else {
        accountsSideMenu.style.display = "block";
    }
};
