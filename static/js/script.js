
$(document).ready(function () {

  $("#back").click(function () {
    window.history.back();
  });

  $(".each__post").click(function () {
    window.location = $(this).find("a").attr("href");
    return false
  });

  $("#DarkSwitch").click(function () {
    $("body").toggleClass("bg-dark");
    $(".lightable").toggleClass('text-light');
  });
});
