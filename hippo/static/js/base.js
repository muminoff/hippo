
var ie_version = function() {
	// ----------------------------------------------------------
	// A short snippet for detecting versions of IE in JavaScript
	// without resorting to user-agent sniffing.
	// Credit: James Padolsey
	// Link: https://gist.github.com/padolsey/527683
	// ----------------------------------------------------------
	var undef,
		v = 3,
		div = document.createElement('div'),
		all = div.getElementsByTagName('i');
	while (
		div.innerHTML = '<!--[if gt IE ' + (++v) + ']><i></i><![endif]-->',
		all[0]
	);
	return v > 4 ? v : undef;
}();

var isMobileDevice = (/Android|webOS|iPhone|iPad|iPod|BlackBerry/i)
	.test(navigator.userAgent);

var HippoFrame = {
	init: function() {
		// DOM element map
		this.el = {
			body: $('body'),
			navigation_expand_target: $('.hippo-mobile-top-bar .navigation-expand-target'),
			hippo_frame: {
				container: $('.hippo-frame'),
				navigation: $('.hippo-frame .hippo-navigation'),
				content: $('.hippo-frame .hippo-content')
			}
		};
		this.events();
	},
	equalizeHeights: function() {
		var tallestColumn = Math.max(
			this.el.hippo_frame.navigation.outerHeight(),
			this.el.hippo_frame.content.outerHeight()
		);

		this.el.hippo_frame.navigation.outerHeight(tallestColumn);
		this.el.hippo_frame.content.outerHeight(tallestColumn);
	},
	dumbSnappingFallback: function() {
		var that = this;
		this.el.navigation_expand_target.click(function() {
			that.el.hippo_frame.navigation.css({
				'z-index': '10'
			}).show();
			return false;
		});

		this.el.hippo_frame.content.click(function() {
			that.el.hippo_frame.navigation.hide();
		});
	},
	setupSnapping: function() {
		if (ie_version && ie_version <= 9) {
			this.dumbSnappingFallback();
		}

		var snapper = new Snap({
			element: this.el.hippo_frame.content[0],
			disable: 'right',
			maxPosition: 250,
			minPosition: -250
		});

		if (!isMobileDevice) {
			this.el.body.attr('data-snap-ignore', 'true');
		}

		this.el.navigation_expand_target.click(function() {
			if (snapper.state().state == "left") {
				snapper.close();
			} else {
				snapper.open('left');
			}
			return false;
		});

		this.snapper = snapper;
	},


	events: function() {
		this.equalizeHeights();
		this.setupSnapping();
	}
};

// Initialize modules when DOM is ready
jQuery(function() {
	HippoFrame.init();
});
