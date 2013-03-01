( function ( w , $ , undefined ) {

  $('html').removeClass('no-js').addClass('js');

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type)) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });

  $('.select-button-list li a').click(function(){
    li = $(this).parent('li');
    checkbox = $('[type=checkbox]', li);
    if (checkbox.is(':checked')) {
      checkbox.prop('checked', false);
      li.removeClass('active');
    } else {
      checkbox.prop('checked', true);
      li.addClass('active');
    }
    return false;
  });

}( window , window.jQuery ));
