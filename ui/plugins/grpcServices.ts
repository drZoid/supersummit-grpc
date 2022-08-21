import { WesternMoviesClient } from "@shwetank/grpc-protobuf-client-js/Western_moviesServiceClientPb";

declare module "#app" {
  interface NuxtApp {
    $movieClient: WesternMoviesClient;
  }
}

export default defineNuxtPlugin(nuxtApp => {
  const baseUrl = nuxtApp.$config.public.baseUrl as string
  const $movieClient = new WesternMoviesClient(baseUrl, null, {
    withCredentials: true
  })

  return {
    provide: {
      movieClient: $movieClient
    }
  }
})
