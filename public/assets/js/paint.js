window.Global = window.Global || {};
    $(function(){
        var main = $('.article_paintblock'),
            canvas = $('<div class="pixel_canvas"></div>'),
            table = $('<table  cellspacing="0" class="pixel_table"></table>'),
            row = $('<tr class="pixel_row"></tr>'),
            col = $('<td class="pixel_col"></td>'),
            isLeftMouseClicked = false,
            size = 28;
        
        canvas.append($('<div class="clear_button">&#9984</div>'));
        function fill(parent, child, size) {
            var clone;
            for(var i = 0; i < size; i += 1) {
                clone = child.clone();
                parent.append( clone );
                if( child.prop("tagName") === 'TR' ) {
                    fill(clone, col, 28)
                }
            }
        }
        fill(table, row, 28);
        canvas.append( table );
        main.append( canvas );

        $(document).on('mousedown', ()=>{
            isLeftMouseClicked = true;
            return false;
        });

        $(document).on('mouseup', ()=>{
            isLeftMouseClicked = false;
        });

        $(canvas).on('mousemove', (e)=>{
            if(isLeftMouseClicked) {
                $(e.target).addClass('active');
            }
        });

        $('.clear_button').on('click', function(e) {
            $('.pixel_col').removeClass('active');
        });

        Global.getPaintedCalls = function() {
            var res = [];
            $('.pixel_col').each((i, el)=>{
                res.push( new Number(5 * $(el).hasClass('active')).valueOf() );
            });
            return res;
        }
    });
