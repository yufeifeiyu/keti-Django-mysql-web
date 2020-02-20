/**
 * Created by yufei on 2018/7/19.
 */


alert("1");
$("#reg1").click(function () {
    alert("Hello world!");
});
$(document).ready(function () {

});

$(document).ready(
    $("#reg11").change(function () {
        alert("2");

    }),
    $("#reg1").click(function () {
        alert("2");

    }));