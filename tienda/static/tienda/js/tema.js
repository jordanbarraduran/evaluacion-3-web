$(document).ready(function () {
    // cambiar data-bs-theme con toggle
    $('#btn-tema').on('click', function () {
      // cambiar en click si es light a dark y viceversa
      if ($('body').attr('data-bs-theme') == 'light') {
        $('body').attr('data-bs-theme', 'dark');
        $('#toggler-tema').removeClass('bi-brightness-high-fill').addClass('bi-moon-fill');
      } else {
        $('body').attr('data-bs-theme', 'light');
        $('#toggler-tema').removeClass('bi-moon-fill').addClass('bi-brightness-high-fill');    
      }});
    });