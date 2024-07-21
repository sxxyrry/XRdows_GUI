//禁用右键（防止右键查看源代码） 
window.oncontextmenu = function() {
        return void 0 ;
}
//禁止任何键盘敲击事件（防止F12和shift+ctrl+i调起开发者工具） 
window.onkeydown = window.onkeyup = window.onkeypress = function() {
    window.event.returnValue = false;
    return void 0 ;
}