$(".datepicker").each(function(){new Pikaday({field:this})});
$('#img_number').on('change keyup', function() {
    var sanitized = $(this).val().replace(/[^0-9]/g, '');
    $(this).val(sanitized);

    if(sanitized > 92 || sanitized < 1)
    {
      $(this).val('');
    }

    if($('#name').val() != "" && $('#img_number').val() != "")
    {
      $('#btn_submit').prop('disabled', false);
    }else
    {
      $('#btn_submit').prop('disabled', true);
    }

  });

$('#name').on('change keyup', function() {
  var letters = /^[A-Za-z ]+$/;
  if(!$(this).val().match(letters))
  {
    var sanitized = $(this).val().replace(/[^A-Za-z ]/g, '');
    $(this).val(sanitized);
  }

  if($('#name').val() != "" && $('#img_number').val() != "")
  {
    $('#btn_submit').prop('disabled', false);
  }
  else
  {
    $('#btn_submit').prop('disabled', true);
  }

});

$('#btn_submit').prop('disabled', true);

