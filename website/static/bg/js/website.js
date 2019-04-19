/* 设置警告提示条的自动关闭时间 */
window.setTimeout(function() {
    $('[role="alert"]').alert('close');
},3000);

/* 全选所有 */
function check_all(){
    $("input[type='checkbox']").prop("checked",true);
}

/* 取消全选所有 */
function deselect_all(){
    $("input[type='checkbox']").prop("checked",false);
}
/* 弹出框 */
$(function () {
    $('[data-toggle="popover"]').popover()
})