//ejecutar función en el evento click
document.getElementById("btn_open").addEventListener("click", open_close_menu)
//declaramos variables

var menu_site = document.getElementById("menu_site")
var body =  document.getElementById("body")
var btn_open = document.getElementById("btn_open")

//función para cambiar de clases
    function open_close_menu(){
        body.classList.toggle("body_move")
        menu_site.classList.toggle("menu-site_move")
    }