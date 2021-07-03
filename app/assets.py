"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle


def compile_static_assets(assets):
    """Configure and build asset bundles."""
    main_style_bundle = Bundle('src/less/*.less',
                               filters='less,cssmin',
                               output='dist/css/landing.css',
                               extra={'rel': 'stylesheet/css'})  # Main Stylesheets Bundle
    main_js_bundle = Bundle('src/js/*.js',
                            filters='jsmin',
                            output='dist/js/main.min.js')  # Main JavaScript Bundle
    assets.register('main_styles', main_style_bundle)
    assets.register('main_js', main_js_bundle)
    if app.config['FLASK_ENV'] == 'development':  # Only rebuild bundles in development
        print("Rebuilding assets...")
        main_style_bundle.build()
        main_js_bundle.build()
    return assets
