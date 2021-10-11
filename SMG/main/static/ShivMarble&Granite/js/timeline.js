function Timeline(selector, config) {
  this.el = $(selector);
  
  // options do not effect CSS, has to be set seperately
  const defaults = {
    track: {
      endAtLast: false
    },
    viewPointBottom: false,
    viewPoint: 400
  }
  this.options = $.extend({}, defaults, config || {})
  
  $(document).ready(() => {
    this.init()
  })
  
  this.init = function() {
    this.el.addClass('is-loading')
    this.el.addClass('is-init')
    this.el.each(function() {this.offsetHeight})
    this.el.removeClass('is-loading')
    this.animation()
    this.trackHeight()
    
    let self = this
    $(document).scroll(function() {
      self.animation()
    })
    $(document).resize(function() {
      self.trackHeight()
    })
  }
  
  this.animation = function() {
    let self = this
    
    let scrollTop = $(document).scrollTop()
    let viewPoint = scrollTop + this.options.viewPoint
    if (this.options.viewPointBottom) {
      viewPoint = scrollTop + window.innerHeight - this.options.viewPoint
    }

    this.updateTrack(viewPoint)

    $('.timeline__item', this.el).each(function(i, v) {
      let top = $(this).offset().top
      let bottom = $(this).offset().top + $(this).outerHeight(true)

      if (viewPoint < top) {
        self.updateClasses(this, 'is-below')

      } else if (viewPoint > bottom) {
        self.updateClasses(this, 'is-above is-visible')
      } else {
        self.updateClasses(this, 'is-current is-visible')
      }
    })
    
    if ($('.timeline__footer').length) {
      let footer = '.timeline__footer'
      let top = $(footer).offset().top

      if (viewPoint < top) {
        self.updateClasses(footer, '')
      } else {
        self.updateClasses(footer, 'is-visible')
      }
    }
  }
  
  this.updateClasses = function(el, newClass) {
    $(el).removeClass('is-above is-current is-below is-visible')
    $(el).addClass(newClass)
  }
  
  this.updateTrack = function(viewPoint) {
    $el = $('.timeline__track', '.timeline')
    let top = $el.offset().top
    let height = viewPoint - top
    $el.height(height)
  }
  
  this.trackHeight = function() {
    let trackMax =  this.el.outerHeight()
    if ($('.timeline__footer').length) {
      trackMax -= $('.timeline__footer').outerHeight()
    }
    if (this.options.track.endAtLast) {
      trackMax = trackMax - $('.timeline__item').last().outerHeight() + 9
    }
    $('.timeline__track', this.el).css('max-height', trackMax)
  }
}

new Timeline('.timeline')