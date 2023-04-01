<script lang="ts">
</script>

<svelte:head>
	<title>Homepage</title>
	<link rel="stylesheet" href="https://unpkg.com/@picocss/pico@1.*/css/pico.min.css" />
</svelte:head>

<main>
	<hgroup id="titles">
		<h1>Welcome to our project!</h1>
		<h2>Built for Axxess Hacakathon 2023 project.</h2>
	</hgroup>
</main>

<!-- Feel free to look through https://picocss.com/docs/typography.html for CSS styling (since it's already imported). -->
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

	#titles {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
</style>
