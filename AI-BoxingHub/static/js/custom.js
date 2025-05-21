(function($){
	$(document).ready(function(){
	
        // var imagePath = "static/images/brain-boxing.jpg";
        // $(".banner-image").backstretch(imagePath);
		
		// Fixed header
		//-----------------------------------------------
		$(window).scroll(function() {
			if (($(".header.fixed").length > 0)) { 
				if(($(this).scrollTop() > 0) && ($(window).width() > 767)) {
					$("body").addClass("fixed-header-on");
				} else {
					$("body").removeClass("fixed-header-on");
				}
			};
		});

		$(window).load(function() {
			if (($(".header.fixed").length > 0)) { 
				if(($(this).scrollTop() > 0) && ($(window).width() > 767)) {
					$("body").addClass("fixed-header-on");
				} else {
					$("body").removeClass("fixed-header-on");
				}
			};
		});
		
	   $('#quote-carousel').carousel({
		 pause: true,
		 interval: 4000,
	   });
		//Scroll Spy
		//-----------------------------------------------
		if($(".scrollspy").length>0) {
			$("body").addClass("scroll-spy");
			$('body').scrollspy({ 
				target: '.scrollspy',
				offset: 152
			});
		}

		//Smooth Scroll
		//-----------------------------------------------
		if ($(".smooth-scroll").length>0) {
			$('.smooth-scroll a[href*=#]:not([href=#]), a[href*=#]:not([href=#]).smooth-scroll').click(function() {
				if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
					var target = $(this.hash);
					target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
					if (target.length) {
						$('html,body').animate({
							scrollTop: target.offset().top-151
						}, 1000);
						return false;
					}
				}
			});
		}

		// Animations
		//-----------------------------------------------
		if (($("[data-animation-effect]").length>0) && !Modernizr.touch) {
			$("[data-animation-effect]").each(function() {
				var $this = $(this),
				animationEffect = $this.attr("data-animation-effect");
				if(Modernizr.mq('only all and (min-width: 768px)') && Modernizr.csstransitions) {
					$this.appear(function() {
						setTimeout(function() {
							$this.addClass('animated object-visible ' + animationEffect);
						}, 400);
					}, {accX: 0, accY: -130});
				} else {
					$this.addClass('object-visible');
				}
			});
		};

		// Like and love buttons - start
		let like = parseInt(document.querySelector('#score_like').innerHTML);
		let love = parseInt(document.querySelector('#score_love').innerHTML);
	
		document.querySelector('#add_like').onclick = function() {
			like += 1;
			document.querySelector('#score_like').innerHTML = like;
			updateLikeInDatabase(like);
		}
	
		document.querySelector('#add_love').onclick = function() {
			love += 1;
			document.querySelector('#score_love').innerHTML = love;
			updateLoveInDatabase(love);
		}

		// Function to get CSRF token from cookies
		function getCookie(name) {
			let cookieValue = null;
			if (document.cookie && document.cookie !== '') {
				const cookies = document.cookie.split(';');
				for (let i = 0; i < cookies.length; i++) {
					const cookie = cookies[i].trim();
					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) === (name + '=')) {
						cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
						break;
					}
				}
			}
			return cookieValue;
		}

		const csrftoken = getCookie('csrftoken');

		// Setting up AJAX to include CSRF token
		$.ajaxSetup({
			beforeSend: function(xhr, settings) {
				if (!/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type) && !this.crossDomain) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			}
		});

		function updateLikeInDatabase(newLike) {
			$.ajax({
				type: 'POST',
				url: '/update_like/',
				data: {
					like: newLike,  // Sending 'like' as data field
					csrfmiddlewaretoken: csrftoken
				},
				success: function(response) {
					// Handle success
					console.log('Like updated successfully');
				},
				error: function(xhr, status, error) {
					// Handle error
					console.error('Error updating like:', error);
				}
			});
		}
		
		function updateLoveInDatabase(newLove) {
			$.ajax({
				type: 'POST',
				url: '/update_love/',
				data: {
					love: newLove,  // Sending 'love' as data field
					csrfmiddlewaretoken: csrftoken
				},
				success: function(response) {
					// Handle success
					console.log('Love updated successfully');
				},
				error: function(xhr, status, error) {
					// Handle error
					console.error('Error updating love:', error);
				}
		
			});
		}		
		// Like and love buttons - end

        // Daytime and nighttime favicon switch
		function setFavicon() {
			console.log("Method called.")
			const now = new Date();
			const hours = now.getHours();
			const favicon = document.getElementById("favicon");
		
			if (hours >= 6 && hours < 18) { // Daytime (6 AM to 6 PM)
				favicon.href = "/static/images/logo-white-circle.png";
			} else { // Nighttime (6 PM to 6 AM)
				favicon.href = "/static/images/logo-black-circle.png";
			}
		}
	
		// Call the function initially and set a timer to update every minute
		setFavicon();
		setInterval(setFavicon, 60000); // Update every minute

	}); // End document ready
})(this.jQuery);
