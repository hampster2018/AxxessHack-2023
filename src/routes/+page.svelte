<script lang="ts">
</script>

<svelte:head>
	<title>Homepage</title>
	<link rel="stylesheet" href="https://unpkg.com/@picocss/pico@1.*/css/pico.min.css" />
</svelte:head>

<main>
	<h1>Welcome to our project!</h1>
</main>

<style lang="scss">
	:global(body),
	:global(html) {
		margin: 0;
		padding: 0;
	}

	main {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
</style>
