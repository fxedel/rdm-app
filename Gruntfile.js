module.exports = function (grunt) {
 'use strict';
 grunt.initConfig({
  bower: {
   libs: {
    options: {
     targetDir: 'static/libs',
     install: true,
     copy: true,
     cleanup: true,
     layout: 'byComponent'
    }
   }
  },
  uglify: {
   build: {
    files: [{
     dest: './static/js/rdm.js',
     src: './js_src/rdm.js'//TODO(dave): change this to ./js_scr/*js
    }],
    options: {
     mangle: true,
     sourceMap: true,
     sourceMapName: './static/js/rdm.js.map'
    }
   }
  },
  karma: {
   firefox: {
    configFile: './unit-test-js/karma.conf.js',
    singleRun: true,
    browsers: ['Firefox'],
    reporters: 'dots',
    plugins: [
     'karma-firefox-launcher',
     'karma-jasmine'
    ]
   },
   chrome: {
    configFile: './unit-test-js/karma.conf.js',
    singleRun: true,
    browsers: ['Chrome'],
    reporters: 'dots',
    plugins: [
     'karma-chrome-launcher',
     'karma-jasmine'
    ]
   }
  },
  jshint: {
   dev: [
    'Gruntfile.js',
    'js_src/rdm.js',//TODO(dave): change this to ./js_scr/*js
    'unit-test-js/karma.conf.js',
    'unit-test-js/tests/*js'
   ],
   options: {
    jshintrc: true
   }
  },
  watch: {
   build: {
    files: ['Gruntfile.js', 'js_src/rdm.js'],
    tasks: ['jshint:dev', 'uglify:build'],
    options: {
     atBegin: true
    }
   }
  }
 });
 grunt.loadNpmTasks('grunt-karma');
 grunt.loadNpmTasks('grunt-bower-task');
 grunt.loadNpmTasks('grunt-contrib-uglify');
 grunt.loadNpmTasks('grunt-contrib-jshint');
 grunt.registerTask('default', ['bower']);
 grunt.registerTask('unit-test', ['bower', 'compress', 'karma:firefox']);
 grunt.registerTask('compress', ['jshint:dev', 'uglify:build']);
 grunt.registerTask('compress-watch', ['watch:build']);
};
