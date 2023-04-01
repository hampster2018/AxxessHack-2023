<script lang="ts">
</script>

<svelte:head>
	<title>Homepage</title>
</svelte:head>

<main>
	<hgroup id="titles">
		<h1>Welcome to our project!</h1>
		<h2>Built for Axxess Hacakathon 2023 project.</h2>
	</hgroup>
</main>

<!-- Feel free to look through https://picocss.com/docs/typography.html for CSS styling (since it's already imported). -->
<style lang="scss">
	main {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		animation: fade 1.5s;
		width: 100svw;
		height: 100svh;
	}

	#titles {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	@keyframes fade {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}
</style>
