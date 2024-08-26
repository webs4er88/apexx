  $(document).ready(function () {
      $('.dropdown-button').dropdown({
          inDuration: 300,
          outDuration: 225,
          constrainWidth: true, // Does not change width of dropdown to that of the activator
          hover: false, // Activate on hover
          gutter: 0, // Spacing from edge
          belowOrigin: true, // Displays dropdown below the button
          alignment: 'left', // Displays dropdown with edge aligned to the left of button
          stopPropagation: false // Stops event propagation
      });
      $('.button-collapse').sideNav();

      $(".carousel.carousel-slider").carousel({
          fullWidth: true
      });

      $('.datepicker').on('mousedown', function(e){
          e.preventDefault();
      })
      $('.datepicker').pickadate({
          selectMonths: true, // Creates a dropdown to control month
          selectYears: 15, // Creates a dropdown of 15 years to control year,
          today: 'Today',
          clear: 'Clear',
          close: 'Ok',
          closeOnSelect: true // Close upon selecting a date,
      });
      $(".slider").slider();
      $('.parallax').parallax();
      $('select').material_select();
    


  });
