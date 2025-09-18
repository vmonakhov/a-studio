module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    proxy: {
      '^/js': {
        target: 'http://10.100.194.95:8080'
      }
    }
  },
  css: {
    loaderOptions: {
      sass: {
        implementation: require('sass'),
        sassOptions: {
          quietDeps: true
        }
      },
      scss: {
        implementation: require('sass'),
        sassOptions: {
          quietDeps: true
        }
      },
    },
  },
};
