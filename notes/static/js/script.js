$(document).ready(function () {
    function updateText(btn, newCount, verb) {
        btn.text(newCount + " " + verb)
        btn.attr("data-likes", newCount)
    }
    $("button[name='badge-info']").click(function (e) {
        e.preventDefault()
        var this_ = $(this)
        var likeUrl = this_.attr("data-href")
        var likeCount = parseInt(this_.attr("data-likes")) | 0
        var addLike = likeCount + 1
        var removeLike = likeCount - 1
        if (likeUrl) {
            $.ajax({
                url: likeUrl,
                method: "GET",
                data: {},
                success: function (data) {
                    console.log(data)
                    if (data.liked) {
                        updateText(this_, addLike, "Likes")
                    } else {
                        updateText(this_, removeLike, "Likes")
                    }

                }, error: function (error) {
                    console.log(error)
                    console.log("error")
                }
            })
        }

    })
})

$(window).scroll(function() {
    if($(window).scrollTop() + $(window).height() > $(document).height() - 200) {
        $('.page-item').addClass('fixed_button');
    }else{
        $('.page-item').removeClass('fixed_button');
    }
 });

    var CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/';
