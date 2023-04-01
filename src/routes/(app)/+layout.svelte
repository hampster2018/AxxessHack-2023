<svelte:head>
	<link rel="stylesheet" href="https://unpkg.com/@picocss/pico@1.*/css/pico.min.css" />
</svelte:head>

<slot />

<style>
	:global(body),
	:global(html) {
		margin: 0;
		padding: 0;
	}
</style>
