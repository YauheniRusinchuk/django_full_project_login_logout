$(function(){

  $('.comment_form').on('submit', (e)=>{
    e.preventDefault();
    create_comment();
  })

});

function create_comment() {
  $.ajax({
    url: $(this).attr('action'),
    type: 'POST',
    data: {
      comment: $('.text_comment').val(),
      csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
    },
    success : function() {
      $('.text_comment').val("");
    }
  })
}
