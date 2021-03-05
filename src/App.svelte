<script>
  /* component logic will go here */
  import { onMount } from "svelte"

  onMount(async () => {
    console.log("helloooo")
    let foo = await fetch("api/foo")
    let res = await foo.text()
    console.log(res)
  })
</script>
<style>
  /* css will go here */
</style>
<div class="App">
  <header class="App-header">
    <a
      class="App-link"
      href="https://svelte.dev"
      target="_blank"
      rel="noopener noreferrer"
    >
      Learn Svelte
    </a>
  </header>
</div>