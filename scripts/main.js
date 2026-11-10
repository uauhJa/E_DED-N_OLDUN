import { world } from "@minecraft/server";

world.afterEvents.chatSend.subscribe((event) => {
    const message = event.message;

    if (!message.toLowerCase().startsWith("!ses ")) {
        return;
    }

    const word = message.substring(5).trim();

    if (word.toLocaleLowerCase("tr-TR").includes("e")) {
        event.sender.kill();

        world.sendMessage(
            `§c☠ ${event.sender.name} E dedi ve öldü!`
        );
    }
});
