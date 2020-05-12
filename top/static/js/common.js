/** ==========================================================================
 * 共通js
 * 
 * ========================================================================= */

$(function(){
	window.$window = $(window)


	/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	 * main
	 * +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */
	var Main = (function(){
		return {
			/**
			 * initialize
			 */
			init : function(){
				Header.init();
				Device.init();
				this.removeFilter();
			},


			/**
			 * こいつが詠み込まれてフィルターを消すまで画面操作させない
			 */
			removeFilter: function(){
				$('.prefilter').remove();
			},
		
		}
	})();



	/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	 * Header
	 * +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */
	var Header = (function(){
		// define
		var MENU_ICON_CLASS = 'header_menutrigger';
		var MENU_ICON_ACTIVE = MENU_ICON_CLASS + '-active';
		var MENU_ICON_INACTIVE = MENU_ICON_CLASS + '-inactive';
		var MENU_ICON_SELECTOR = '.' + MENU_ICON_CLASS;
		var MENU_CLASS = 'header_menu';
		var MENU_ACTIVE = MENU_CLASS + '-show';
		var MENU_SELECTOR = '.' + MENU_CLASS;
		var _this;
		var OPEN_SPEED = 300;
		var CLOSE_SPEED = 250;
		var status = 'close';
	
		// 
		return {
			/**
			 * initialize
			 */
			init: function(){
				_this = this;
				this.bindMenuTrigger();
				this.adjustMenuPosition();
			},

			/**
			 * ヘッダーのメニューボタン押下時のイベント登録
			 */
			bindMenuTrigger: function(){
				$(MENU_ICON_SELECTOR).on('click', function(){
					var $this = $(this);
					if($this.hasClass(MENU_ICON_ACTIVE)){
						status = 'close';
						$this.removeClass(MENU_ICON_ACTIVE);
						$this.addClass(MENU_ICON_INACTIVE);
						_this.hideMenu();
					}else{
						status = 'open';
						$this.removeClass(MENU_ICON_INACTIVE);
						$this.addClass(MENU_ICON_ACTIVE);
						_this.showMenu();
					}
				})
			},

			/**
			 * show
			 */
			showMenu: function(){
				var $menu = $(MENU_SELECTOR);
				var left = $window.width() - $menu.width();
				$menu.stop().addClass(MENU_ACTIVE);
				$menu.css('transition', (OPEN_SPEED/1000) + 's left ease-out');
				$menu.css('left', left);
			},

			/**
			 * hide
			 */
			hideMenu: function(){
				var $menu = $(MENU_SELECTOR);
				var left = $window.width() + $menu.width();
				$menu.stop();
				$menu.css('transition', (CLOSE_SPEED/1000) + 's left ease-in');
				$menu.css('left', left);
				setTimeout(function(){
					if(status == 'close'){
						$menu.removeClass(MENU_ACTIVE);
					}
				}, CLOSE_SPEED);
			},

			/**
			 * 
			 */
			adjustMenuPosition: function(){
				var $menu = $(MENU_SELECTOR)
				$window.on('resize', function(){
					console.log(window.innerWidth)
					if(window.innerWidth > 700){ 
						var left = ''
					}else if(status = 'open'){
						var left = $window.width() - $menu.width();
					}else{
						var left = $window.width() + $menu.width();
					}
					$menu.css('left', left);
				});
			},
		
		}
	})();



	/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	 * Device
	 * +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */
	var Device = (function(){
		var ua = navigator.userAgent;
		var device = '';
		var browser = '';
		var _this;
		var $body = $('body');
	
		// 
		return {
			/**
			 * initialize
			 */
			init: function(){
				_this = this
				this.setDveiceType();
				this.setBrowser();
				// this.bindDveiceType();
			},


			/**
			 * 
			 */
			bindDveiceType: function(){
				$window.on('resize', function(){
					_this.setDeviceType();
				});
			},

			/**
			 * 
			 */
			setDveiceType: function(){
				if (ua.indexOf('iPhone') > -1 || (ua.indexOf('Android') > -1 && ua.indexOf('Mobile') > -1)) {
					device = 'smartphone';
					$body.removeClass('pc');
					$body.addClass('sp');
				} else if (ua.indexOf('iPad') > -1 || ua.indexOf('Android') > -1) {
					device = 'tablet';
					$body.removeClass('pc');
					$body.addClass('sp');
				} else {
					device = 'pc';
					$body.removeClass('sp');
					$body.addClass('pc');
				}
			},

			/**
			 * 
			 */
			setBrowser: function(){
				var userAgent = ua.toLowerCase();
				if(userAgent.indexOf('msie') != -1 || userAgent.indexOf('trident') != -1) {
					browser = 'ie';
				} else if(userAgent.indexOf('edge') != -1) {
					browser = 'edge';
				} else if(userAgent.indexOf('chrome') != -1) {
					browser = 'chrome';
				} else if(userAgent.indexOf('safari') != -1) {
					browser = 'safari';
				} else if(userAgent.indexOf('firefox') != -1) {
					browser = 'firefox';
				} else if(userAgent.indexOf('opera') != -1) {
					browser = 'opera';
				} else {
					browser = 'unkrown';
				}
			},
		}

	})();


	/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	 * FadeIn Contents
	 * +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */
	var FadeIn = (function(){
		// define
		var STANDBY_CLASS = 'fade-in'
		var LOCK_CLASS = STANDBY_CLASS + '-lock' // animation実行中にロックする
		var STANDBY_SELECTOR = '.' + STANDBY_CLASS // scrollしたら表示される要素
		var SHOW_START = 100 // ?px前にきたら表示させるか
		var FADEIN_DISTANCE = 120 // ?px下から表示させるか
		var SPEED_DEFAULT = 1000 // 表示スピード
		var _this
	
		// 
		return {
			/**
			 * initialize
			 */
			init : function(){
				_this = this
				this.bind()
				this.setTransform()
				this.showBlock()
			},

			/**
			 * 初期値をセットします
			 */
			setTransform : function(){
				$(STANDBY_SELECTOR).css({'transform': 'translateY('+ FADEIN_DISTANCE +'px)'})
			},

			/**
			 * bind
			 */
			bind : function(){
				$window.on('scroll.display', function(){
					_this.showBlock()
				})
			},

			/**
			 * unbind
			 */
			unbind : function(){
				$window.off('scroll.display')
			},

			/**
			 * 
			 */
			showBlock : function(){
				var $standby =  $(STANDBY_SELECTOR)
				var standbynNum = $standby.length
				if(standbynNum === 0) return;
				var scrollY = $window.scrollTop() + $window.height() - SHOW_START
				var speed, top, before_top, parallel_count = 0
				// 表示されていない要素をみていく
				$standby.each(function(){
					var $this = $(this)
					if($this.hasClass(LOCK_CLASS)) return true
					top = parseInt($this.offset().top)
					// 横並びの要素は表示時間をずらす
					if(top === before_top){
						parallel_count++
					}else{
						parallel_count = 0	
					}
					if(top < scrollY){
						speed = parseInt($this.data('fadein_speed') || SPEED_DEFAULT) || 0
						standbynNum--
						before_top = top
						$this.addClass(LOCK_CLASS)
						setTimeout(function(){
							// 下から上へFADEIN_START
							$this.css({'transition': 'transform ' +  (speed / 1000) + 's'})
							$this.css({'transform': 'translateY(0px)'})
							// 透明度をなくす
							$this.animate({opacity: 1}, {duration: speed, easing: 'swing'})
							// 表示されたあとの処理
							setTimeout(function(){
								$this.removeClass(STANDBY_CLASS)
								$this.removeClass(LOCK_CLASS)
								$this.css({'transition': '', 'transform': '', 'opacity': ''})
							}, speed)
						}, 200 * parallel_count)
						// if(RecruitInformation.isSelector($this)){
						// 	setTimeout(function(){
						// 		console.log('aaa');
						// 		RecruitInformation.adjustInformationBox()
						// 	}, 10)
						// }
					}else{
						return false
					}
					before_top = top
				})
				// 全部表示されたらイベント不要
				if(standbynNum === 0){
					_this.unbind()
				}
			},

			/**
			 * @return {integer} 
			 */
			getFadeInDistance: function(){
				return FADEIN_DISTANCE
			},

			/**
			 * @return {string} 
			 */
			getFadeInClass: function(){
				return STANDBY_CLASS
			}
		
		}
	})();






	//最初に実行
	Main.init()
});
