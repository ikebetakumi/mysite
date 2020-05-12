/** ==========================================================================
 * 季節js
 * 
 * ========================================================================= */

$(function(){


	/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	 * main
	 * +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */
	var Main = (function(){
		return {
			/**
			 * initialize
			 */
			init : function(){
				this.setGlobal();
				SnowDrop.init();
			},


			/**
			 * 
			 */
			setGlobal: function(){
				window.snowDrop = SnowDrop;
			},
		
		}
	})();



	/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	 * SnowDrop
	 * +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */
	var SnowDrop = (function(){
		// define
		var SOURCE = '.source';
		var TARGET_INNER_CLASS = 'showdropBack';
		var DEFAULT_TARGET = '.snowdrop';
		var IMAGE_SPRING = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAPCAYAAADQ4S5JAAABJ0lEQVR42o2RvUoDQRRGz8w6NiKERGOhFiKDVmm0E3wAmyGN4Buk0uewiK2dIFhYCROxSWFlIWplocJIAiGLIrIIEVEnYW2SqHEj+1Ufl3vur3gsn0a5+ZkKQlSAE2X0B/9IhNvVGCC/OAcQAQdAWRndSAJkZjpPw9V5fXgGyAKbwL23btdbl/sDjI6PvefyE9Su74jbnV5cASXg1lu39gsAWrOFBYKRgM/W22DBSeDYW1fq7+CtuwKWAIhjECJp9BgoKqOtBG6+TyCGHgfY89ZlJHBBOmWBLQlUSa+iAPDWXQLLKYCO7JqdlB2CHnAInA1JegGeuj6UAMroGNgAwgRgXxk91X1mQfZfa3QTWAXOk9ooo9vK6EgOBGvACrAOHAF1wP/M+QLaVlMwZrBk6gAAAABJRU5ErkJggg==';
		var IMAGE_SUMMER = '';
		var IMAGE_AUTUMN = '';
		var IMAGE_SUMMER = '';
		var DROP_SPEED = 3; // s/100px
		var _this;
		var count = 0;
		
		// 
		return {
			/**
			 * initialize
			 */
			init: function(){
				_this = this;
				$(DEFAULT_TARGET).each(function(){
					_this.set($(this));
				});
			},

			set: function($target, $targetsnow){
				count++;
				var targetHight = $target.height();
				var targetWidth = $target.width();
				// create show background
				$target.append('<div class="'+TARGET_INNER_CLASS+'"></div>');
				var $target = $target.find('.'+TARGET_INNER_CLASS);
				$target.css({
					'position': 'absolute',
					'top': 0,
					'left': 0,
					'width': '100%',
					'height': '100%',
					'z-index': -1
				});
				// create show
				if($targetsnow === void 0){
					$targetsnow = _this.getSeasonImage($target);
				}
				var $clone = $targetsnow.clone();
				var snowHeight = $clone.height();
				var snowWidth = $clone.width();
				var i_max = Math.round(targetHight / 100) || 1;
				var j_max = Math.round(targetWidth / (snowWidth*10));
				_this.setKeyFrame(targetHight, targetWidth/j_max);
				for (var i = 0; i < i_max; i++) {
					if(i%2==1) continue;
					for (var j = 0; j < j_max; j++) {
						var type = _this.getRandom(-1,1);
						var typename = type == 0  ? 'center' : (type==-1 ? 'left':'right');
						var $clone2 = $clone.clone();
						var delay = _this.getRandom(0,DROP_SPEED*10) / 10;
						if(_this.getRandom(0,1) == 0){
							delay *= -1;
						}
						var per = _this.getRandom(50,100) / 100;
						var h = parseInt(snowHeight*per);
						var w = parseInt(snowWidth*per);
						$clone2.css({
							'opacity': '0',
							'position': 'absolute',
							'display': 'inline-block',
							'-webkit-transform-origin': '0px 0px',
							'-ms-transform-origin': '0px 0px',
							'transform-origin': '0px 0px',
							'-webkit-animation-name': 'Drop'+count+'_'+typename,
							'animation-name': 'Drop'+count+'_'+typename,
							'-webkit-animation-iteration-count': 'infinite',
							'animation-iteration-count': 'infinite',
							'-webkit-animation-timing-function': 'linear',
							'animation-timing-function': 'linear',
							'-webkit-animation-fill-mode': 'forwards',
							'animation-fill-mode': 'forwards',
							'left': (j*snowWidth*10) + 'px',
							'-webkit-animation-duration': (DROP_SPEED*i_max)+'s',
							'animation-duration': (DROP_SPEED*i_max)+'s',
							'-webkit-animation-delay': (DROP_SPEED*i + delay)+'s',
							'animation-delay': (DROP_SPEED*i + delay)+'s',
							'width': w+'px',
							'height': h+'px',
						});
						$target.append($clone2);
					}
					$clone.remove();
				}
			},

			getSeasonImage: function($target){
				var image;
				var date = new Date();
				var month = date.getMonth() + 1;
				if(month >= 3 && month <= 5){
					image = IMAGE_SPRING;
				}
				if(month >= 6 && month <= 8){
					image = IMAGE_SUMMER;
				}
				if(month >= 9 && month <= 11){
					image = IMAGE_AUTUMN;
				}
				if(month >= 12 && month <= 2){
					image = IMAGE_SUMMER;
				}
				$target.append('<div class="drops'+count+'" style="width:10px;height:15px;"></div>');
				var style = '';
				style += '<style type="text/css">';
				style += '<!--';
				style += '.drops'+count+' {';
				style += 'display: none;';
				style += 'background: url(\''+image+'\') no-repeat;';
				style += '}';
				style += '-->';
				style += '</style>';
				$(SOURCE).append(style);
				return $target.find('.drops'+count);
			},

			/**
			 *
			 */
			setKeyFrame: function(height, x){
				var array = [0, 20, 40, 60, 80, 100];
				var style = '';
				style += '<style type="text/css">';
				style += '<!--';
				
				for (var type = -1; type <= 1; type++) {
					var typename = type == 0  ? 'center' : (type==-1 ? 'left':'right');
					var style_body = '';
					for (var index = 0; index < array.length; index++) {
						var per = array[index];
						var _x = (x*type*0.2)*(index%3-1);
						var y = height * per / 100;
						style_body += ' '+per+'% {';
						style_body += '  -webkit-transform: translate('+_x+'px,'+ y +'px);';
						style_body += '  transform: translate('+_x+'px, '+ y +'px);';
						if(per==100||per==0){
							style_body += '  opacity: 0;';
						}else{
							style_body += '  opacity: 1;';
						}
						style_body += ' }';
					}
					style += '@-webkit-keyframes Drop'+count+'_'+typename+' {';
					style += style_body;
					style += '}';

					style += '@keyframes Drop'+count+' {';
					style += style_body;
					style += '}';
				}

				style += '-->';
				style += '</style>';
				$(SOURCE).append(style);
			},

			getRandom: function( min, max ) {
				var random = Math.floor( Math.random() * (max + 1 - min) ) + min;
				return random;
			}
		
		}
	})();




	//最初に実行
	Main.init()
});
