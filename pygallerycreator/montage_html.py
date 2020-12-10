html = """

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Gallery</title>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
        <link rel="shortcut icon" href="../favicon.ico"> 
        <link rel="stylesheet" type="text/css" href="montage/css/demo.css" />
        <link rel="stylesheet" type="text/css" href="montage/css/style.css" />
        <link href='https://fonts.googleapis.com/css?family=PT+Sans+Narrow&v1' rel='stylesheet' type='text/css' />
        <link href='https://fonts.googleapis.com/css?family=Monoton' rel='stylesheet' type='text/css' />
        <link rel="stylesheet" type="text/css" href="lightbox/css/lightbox.min.css"/>
    </head>
    <body>
        <div class="container">
            <div class="header">
               
            </div>
			<div class="am-container" id="am-container">
				<!-- images go here -->
				<!-- <a href="#"><img src="images/1.jpg"></img></a> -->
				{% for image in images %}
                <a href="large_imgs/{{image}}" data-lightbox="gallery" data-title="{{image}}"><img src="thumbs/{{image}}"></img></a>
                {% endfor %}
			</div>
        </div>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js"></script>
        <script type="text/javascript" src="lightbox/js/lightbox.min.js"></script>
        <script type="text/javascript" src="montage/js/jquery.montage.min.js"></script>
        <script type="text/javascript">
            $(function() {
                /* 
                 * just for this demo:
                 */
                $('#showcode').toggle(
                    function() {
                        $(this).addClass('up').removeClass('down').next().slideDown();
                    },
                    function() {
                        $(this).addClass('down').removeClass('up').next().slideUp();
                    }
                );
                $('#panel').toggle(
                    function() {
                        $(this).addClass('show').removeClass('hide');
                        $('#overlay').stop().animate( { left : - $('#overlay').width() + 20 + 'px' }, 300 );
                    },
                    function() {
                        $(this).addClass('hide').removeClass('show');
                        $('#overlay').stop().animate( { left : '0px' }, 300 );
                    }
                );
                
                var $container  = $('#am-container'),
                    $imgs       = $container.find('img').hide(),
                    totalImgs   = $imgs.length,
                    cnt         = 0;
                
                $imgs.each(function(i) {
                    var $img    = $(this);
                    $('<img/>').load(function() {
                        ++cnt;
                        if( cnt === totalImgs ) {
                            $imgs.show();
                            $container.montage({
                                fillLastRow             : false,
                                alternateHeight         : true,
                                alternateHeightRange    : {
                                    min : 90,
                                    max : 240
                                }
                            });
                            
                            /* 
                             * just for this demo:
                             */
                            $('#overlay').fadeIn(500);
                        }
                    }).attr('src',$img.attr('src'));
                }); 
                
            });
        </script>
    </body>
</html>
"""